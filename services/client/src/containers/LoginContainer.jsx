import { connect } from 'react-redux'
import { bindActionCreators } from 'redux'

import Login from '../components/LoginComponent'
import * as loginActions from '../actions/login.action'
import * as userActions from '../actions/user.action'

const actionsCreator = { ...loginActions, ...userActions }

const mapStateToProps = state => {
  return {
    isSending: state.login.isSending,
    isSent: state.login.isSent,
    token: state.login.token,
    username: state.user.username,
    isAdmin: state.user.isAdmin,
    isActive: state.user.isActive,
    isUser: state.user.isUser,
    isAuthenticated: state.user.isAuthenticated,
    isAuthenticating: state.user.isAuthenticating,
    loginMsg: state.login.loginMsg,
    userMsg: state.user.userMsg
  }
}

const mapDispatchToProps = dispatch => {
  return bindActionCreators(actionsCreator, dispatch)
}

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Login)
