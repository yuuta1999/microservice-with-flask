import Login from '../containers/LoginContainer'
import Register from '../containers/RegisterContainer'

const routes = {
  Login: {
    component: Login,
    path: '/login'
  },
  Register: {
    component: Register,
    path: '/register'
  }
}

export default routes
