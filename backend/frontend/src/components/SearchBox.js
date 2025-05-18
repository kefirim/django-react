import React, { useState } from 'react'
import { Button, Form } from 'react-bootstrap'
import { useNavigate } from 'react-router-dom'

function SearchBox() {
    const [keyword, setKeyword] = useState('')
    const navigate = useNavigate()

    const submitHandler = (e) => {
        e.preventDefault()
        if (keyword.trim()) {
            navigate({
                pathname: '/',
                search: `?keyword=${keyword.trim()}&page=1`
            })
        } else {
            // rester sur la page actuelle sans paramètre
            navigate(window.location.pathname)
        }
    }

    return (
        <Form onSubmit={submitHandler} className="d-flex">
            <Form.Control
                type='text'
                name='q'
                onChange={(e) => setKeyword(e.target.value)}
                placeholder="Search products..."
                className='me-2'
            />
            <Button type='submit' variant='outline-success' className='p-2'>
                Search
            </Button>
        </Form>
    )
}

export default SearchBox
