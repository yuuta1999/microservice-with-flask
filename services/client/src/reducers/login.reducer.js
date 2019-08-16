import { Login } from '../constants/login.constant'
import { createReducer } from '../utils/misc'

const initialState = {
  isSending: false,
  isSent: false,
  token: null,
  loginMsg: null
}

export default createReducer(initialState, {
  [Login.REQUEST]: state =>
    Object.assign({}, state, {
      isSending: true,
      loginMsg: 'Sending'
    }),
  [Login.SUCCESS]: (state, payload) =>
    Object.assign({}, state, {
      isSending: true,
      isSent: false,
      token: payload.access_token,
      loginMsg: 'Success'
    }),
  [Login.FAILURE]: (state, payload) =>
    Object.assign({}, state, {
      isSending: false,
      loginMsg: `Authentication error: ${payload.statusText}`
    })
})
