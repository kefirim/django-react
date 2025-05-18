import React, { useState, useEffect } from 'react'
import { Link, useLocation, useNavigate } from 'react-router-dom'
import { Form, Button, Row, Col } from 'react-bootstrap'
import { useDispatch, useSelector } from 'react-redux'
import Loader from '../components/Loader'
import Message from '../components/Message'
import FormContainer from '../components/FormContainer'
import { register } from '../actions/userActions'

function RegisterScreen() {
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [confirmPassword, setConfirmPassword] = useState('')
  const [message, setMessage] = useState('')

  const dispatch = useDispatch()
  const location = useLocation()
  const navigate = useNavigate()

  const redirect = new URLSearchParams(location.search).get('redirect') || '/'

  const userRegister = useSelector(state => state.userRegister)
  const { error, loading, userInfo } = userRegister

  useEffect(() => {
    if (userInfo) {
      navigate(redirect)
    }
  }, [navigate, userInfo, redirect])

  const submitHandler = (e) => {
    e.preventDefault()
    if (password !== confirmPassword) {
      setMessage('Les mots de passe ne correspondent pas')
    } else {
      dispatch(register(name, email, password))
      setMessage('')
    }
  }

  return (
    <FormContainer>
      <h1>Inscription</h1>
      {message && <Message variant='danger'>{message}</Message>}
      {error && <Message variant='danger'>{error}</Message>}
      {loading && <Loader />}
      <Form onSubmit={submitHandler}>
        <Form.Group controlId='name' className='my-2'>
          <Form.Label>Nom</Form.Label>
          <Form.Control
            required
            type='text'
            placeholder='Entrez votre nom'
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </Form.Group>

        <Form.Group controlId='email' className='my-2'>
          <Form.Label>Adresse Email</Form.Label>
          <Form.Control
            required
            type='email'
            placeholder='Entrez votre adresse email'
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </Form.Group>

        <Form.Group controlId='password' className='my-2'>
          <Form.Label>Mot de passe</Form.Label>
          <Form.Control
            required
            type='password'
            placeholder='Entrez votre mot de passe'
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </Form.Group>

        <Form.Group controlId='passwordConfirm' className='my-2'>
          <Form.Label>Confirmer le mot de passe</Form.Label>
          <Form.Control
            required
            type='password'
            placeholder='Confirmez votre mot de passe'
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
          />
        </Form.Group>

        <Button type='submit' variant='primary' disabled={loading}>
          S'inscrire
        </Button>
      </Form>

      <Row className='py-3'>
        <Col>
          Vous avez déjà un compte ?{' '}
          <Link to={redirect ? `/login?redirect=${redirect}` : '/login'}>
            Connectez-vous
          </Link>
        </Col>
      </Row>
    </FormContainer>
  )
}

export default RegisterScreen
