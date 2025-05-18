import React, { useState } from 'react'
import { Form, Button } from 'react-bootstrap'
import { useNavigate } from 'react-router-dom'

import { useDispatch, useSelector } from 'react-redux'
import FormContainer from '../components/FormContainer'
import CheckoutSteps from '../components/CheckoutSteps'
import { saveShippingAddress } from '../actions/cartActions'

function ShippingScreen() {
    const navigate=useNavigate()
    const cart = useSelector(state => state.cart)
    const { shippingAddress } = cart

    const dispatch = useDispatch()

    // Si shippingAddress est vide, on initialise à chaîne vide pour éviter undefined
    const [address, setAddress] = useState(shippingAddress?.address || '')
    const [city, setCity] = useState(shippingAddress?.city || '')
    const [postalCode, setPostalCode] = useState(shippingAddress?.postalCode || '')
    const [country, setCountry] = useState(shippingAddress?.country || '')

    const submitHandler = (e) => {
        e.preventDefault()
        dispatch(saveShippingAddress({ address, city, postalCode, country }))
        navigate('/payment')
    }

    return (
        <FormContainer>
            <CheckoutSteps step1 step2 />
            <h1>Adresse de livraison</h1>
            <Form onSubmit={submitHandler}>

                <Form.Group controlId='address' className="my-2">
                    <Form.Label>Adresse</Form.Label>
                    <Form.Control
                        required
                        type='text'
                        placeholder='Entrez votre adresse'
                        value={address}
                        onChange={(e) => setAddress(e.target.value)}
                    />
                </Form.Group>

                <Form.Group controlId='city' className="my-2">
                    <Form.Label>Ville</Form.Label>
                    <Form.Control
                        required
                        type='text'
                        placeholder='Entrez votre ville'
                        value={city}
                        onChange={(e) => setCity(e.target.value)}
                    />
                </Form.Group>

                <Form.Group controlId='postalCode' className="my-2">
                    <Form.Label>Code postal</Form.Label>
                    <Form.Control
                        required
                        type='text'
                        placeholder='Entrez votre code postal'
                        value={postalCode}
                        onChange={(e) => setPostalCode(e.target.value)}
                    />
                </Form.Group>

                <Form.Group controlId='country' className="my-2">
                    <Form.Label>Pays</Form.Label>
                    <Form.Control
                        required
                        type='text'
                        placeholder='Entrez votre pays'
                        value={country}
                        onChange={(e) => setCountry(e.target.value)}
                    />
                </Form.Group>

                <Button type='submit' variant='primary'>
                    Continuer
                </Button>
            </Form>
        </FormContainer>
    )
}

export default ShippingScreen
