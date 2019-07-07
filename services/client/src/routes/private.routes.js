import Admin from '../containers/AdminContainer'
import Dashboard from '../containers/DashboardContainer'

const routes = {
  Admin: {
    component: Admin,
    path: '/admin'
  },
  Dashboard: {
    component: Dashboard,
    path: '/dashboard'
  }
}

export default routes
