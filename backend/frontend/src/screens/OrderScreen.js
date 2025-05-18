import React, { useEffect } from 'react'
import { Row, Col, ListGroup, Image, Card, Button } from 'react-bootstrap'
import { Link, useParams ,useNavigate} from 'react-router-dom'
import { useDispatch, useSelector } from 'react-redux'
import Message from '../components/Message'
import Loader from '../components/Loader'
import { getOrderDetails, payOrder , deliverOrder } from '../actions/orderActions'
import { ORDER_PAY_RESET, ORDER_DELIVER_RESET  } from '../constants/orderConstants'
import {
    PayPalScriptProvider,
    PayPalButtons,
} from "@paypal/react-paypal-js";

function OrderScreen() {
    const navigate = useNavigate()
    const params = useParams();
    const orderId = params.id;
    const dispatch = useDispatch();

    const orderDetails = useSelector((state) => state.orderDetails);
    const { order, error, loading } = orderDetails;

    const orderPay = useSelector((state) => state.orderPay);
    const { loading: loadingPay, success: successPay } = orderPay;

     const orderDeliver = useSelector(state => state.orderDeliver)
    const { loading: loadingDeliver, success: successDeliver } = orderDeliver

     const userLogin = useSelector(state => state.userLogin)
    const { userInfo } = userLogin

    if (!loading && !error) {
        order.itemsPrice = order.orderItems
            .reduce((acc, item) => acc + item.price * item.qty, 0)
            .toFixed(2);
    }

    useEffect(() => {

        
        if (!userInfo) {
            navigate('/login')
        }
        if (!order || successPay || order._id !== Number(orderId) || successDeliver) {
            dispatch({ type: ORDER_PAY_RESET });
            dispatch(getOrderDetails(orderId));
            dispatch({ type: ORDER_DELIVER_RESET })
        }
    }, [dispatch, order, orderId, successPay,successDeliver,navigate ,userInfo]);

    const successPaymentHandler = (paymentResult) => {
        console.log('Paiement réussi :', paymentResult);
        dispatch(payOrder(orderId, paymentResult));
    };

      const deliverHandler = () => {
        dispatch(deliverOrder(order))
    }

    return loading ? (
        <Loader />
    ) : error ? (
        <Message variant="danger">{error}</Message>
    ) : (
        <PayPalScriptProvider
            options={{
                "client-id": "ASf4GgSQQ1St6SimStVCLHE9Gvxcu2vnI1XFyGma7TnRWOkFi3ltVAkXNWKktYwC7Sv2xxr6sy6M6CUc",
                currency: "USD",
                intent: "capture",
            }}
        >
            <div>
                <h1>Commande : {order._id}</h1>
                <Row>
                    <Col md={8}>
                        <ListGroup variant="flush">
                            <ListGroup.Item>
                                <h2>Livraison</h2>
                                <p><strong>Nom : </strong>{order.user.name}</p>
                                <p><strong>Email : </strong><a href={`mailto:${order.user.email}`}>{order.user.email}</a></p>
                                <p><strong>Adresse : </strong>{order.shippingAddress.address}, {order.shippingAddress.city}, {order.shippingAddress.postalCode}, {order.shippingAddress.country}</p>
                                {order.isDelivered ? (
                                    <Message variant="success">Livrée le {order.deliveredAt}</Message>
                                ) : (
                                    <Message variant="warning">Pas encore livrée</Message>
                                )}
                            </ListGroup.Item>

                            <ListGroup.Item>
                                <h2>Paiement</h2>
                                <p><strong>Méthode : </strong>{order.paymentMethod}</p>
                                {order.isPaid ? (
                                    <Message variant="success">Payée le {order.paidAt}</Message>
                                ) : (
                                    <Message variant="warning">Non payée</Message>
                                )}
                            </ListGroup.Item>

                            <ListGroup.Item>
                                <h2>Articles</h2>
                                {order.orderItems.length === 0 ? (
                                    <Message>La commande est vide</Message>
                                ) : (
                                    <ListGroup variant="flush">
                                        {order.orderItems.map((item, index) => (
                                            <ListGroup.Item key={index}>
                                                <Row>
                                                    <Col md={1}>
                                                        <Image src={item.image} alt={item.name} fluid rounded />
                                                    </Col>
                                                    <Col>
                                                        <Link to={`/product/${item.product}`}>{item.name}</Link>
                                                    </Col>
                                                    <Col md={4}>
                                                        {item.qty} × ${item.price} = ${(item.qty * item.price).toFixed(2)}
                                                    </Col>
                                                </Row>
                                            </ListGroup.Item>
                                        ))}
                                    </ListGroup>
                                )}
                            </ListGroup.Item>
                        </ListGroup>
                    </Col>

                    <Col md={4}>
                        <Card>
                            <ListGroup variant="flush">
                                <ListGroup.Item>
                                    <h2>Résumé</h2>
                                </ListGroup.Item>
                                <ListGroup.Item>
                                    <Row>
                                        <Col>Articles :</Col>
                                        <Col>${order.itemsPrice}</Col>
                                    </Row>
                                </ListGroup.Item>
                                <ListGroup.Item>
                                    <Row>
                                        <Col>Livraison :</Col>
                                        <Col>${order.shippingPrice}</Col>
                                    </Row>
                                </ListGroup.Item>
                                <ListGroup.Item>
                                    <Row>
                                        <Col>Taxe :</Col>
                                        <Col>${order.taxPrice}</Col>
                                    </Row>
                                </ListGroup.Item>
                                <ListGroup.Item>
                                    <Row>
                                        <Col>Total :</Col>
                                        <Col>${order.totalPrice}</Col>
                                    </Row>
                                </ListGroup.Item>

                                {!order.isPaid && (
                                    <ListGroup.Item>
                                        {loadingPay && <Loader />}
                                        <PayPalButtons
  style={{ layout: 'vertical' }}
  createOrder={(data, actions) => {
    return actions.order.create({
      purchase_units: [{
        amount: {
          value: "10000.00",  // Montant fixe à 10 000 dollars
        },
      }],
    });
  }}
  onApprove={(data, actions) => {
    return actions.order.capture().then(details => {
      successPaymentHandler(details);
    });
  }}
/>

                                    </ListGroup.Item>
                                )}
                            </ListGroup>

                             {loadingDeliver && <Loader />}
                                {userInfo && userInfo.isAdmin && order.isPaid && !order.isDelivered && (
                                    <ListGroup.Item>
                                        <Button
                                            type='button'
                                            className='btn btn-block'
                                            onClick={deliverHandler}
                                        >
                                            Mark As Delivered
                                        </Button>
                                    </ListGroup.Item>
                                )}
                        </Card>
                    </Col>
                </Row>
            </div>
        </PayPalScriptProvider>
    );
}

export default OrderScreen;
