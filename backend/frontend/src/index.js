import React from 'react'
import ReactDOM from 'react-dom/client'
import { Provider } from 'react-redux'
import { HashRouter } from 'react-router-dom'
import store from './store'
import './bootstrap.min.css'
import App from './App'
import reportWebVitals from './reportWebVitals'

const root = ReactDOM.createRoot(document.getElementById('root'))
root.render(
  <Provider store={store}>
    <HashRouter>  {/* ✅ Enveloppe App ici */}
      <App />
    </HashRouter>
  </Provider>
)

reportWebVitals()
