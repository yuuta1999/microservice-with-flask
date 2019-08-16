import { combineReducers } from 'redux'

import login from './login.reducer'
import user from './user.reducer'

const rootReducer = combineReducers({
  login,
  user
})

export default rootReducer
