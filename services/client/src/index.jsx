import React from 'react'
import ReactDOM from 'react-dom'
import { Provider } from 'react-redux'
import { createStore, applyMiddleware, compose } from 'redux'
import thunk from 'redux-thunk'

import Root from './template'
import rootReducer from './reducers'
import './assets/styles/main.scss'

const composeEnhancers =
  typeof window === 'object'
    ? window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__
    : compose

const enhancer = composeEnhancers(applyMiddleware(thunk))

const store = createStore(rootReducer, enhancer)

ReactDOM.render(
  <Provider store={store}>
    <Root />
  </Provider>,
  document.getElementById('root')
)
