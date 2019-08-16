import { GetUser } from '../constants/user.constant'
import { createReducer } from '../utils/misc'

const initialState = {
  username: '',
  email: '',
  isUser: false,
  isActive: false,
  isAdmin: false,
  isAuthenticated: false,
  isAuthenticating: false,
  userMsg: ''
}

export default createReducer(initialState, {
  [GetUser.REQUEST]: state =>
    Object.assign({}, state, {
      isAuthenticating: true,
      userMsg: 'Loading user...'
    }),
  [GetUser.SUCCESS]: (state, payload) =>
    Object.assign({}, state, {
      isAuthenticated: true,
      isAuthenticating: false,
      username: payload.username,
      email: payload.email,
      isUser: payload.isUser,
      isActive: payload.isActive,
      isAdmin: payload.isAdmin,
      userMsg: 'Loaded successfully.'
    }),
  [GetUser.FAILURE]: (state, error) =>
    Object.assign({}, state, {
      isAuthenticating: false,
      isAuthenticated: false,
      isUser: false,
      isActive: false,
      isAdmin: false,
      userMsg: `Error happen: ${error.statusText}`
    })
})
