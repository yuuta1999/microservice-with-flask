import React from 'react'
import { Router, Switch, Route } from 'react-router-dom'
import _ from 'lodash'

import Public from './pages/PublicPage'
import Private from './pages/PrivatePage'
import NotFound from './pages/NotFound'
import privateRoutes from './routes/private.routes'
import publicRoutes from './routes/public.routes'
import sessionRoutes from './routes/session.routes'
import { history } from './utils/misc'

const Template = () => {
  return (
    <Router history={history}>
      <Switch>
        {_.map(publicRoutes, (route, key) => {
          const { component, path } = route
          console.log(path)
          return (
            <Route
              exact
              path={path}
              key={key}
              render={r => <Public component={component} route={r} />}
            />
          )
        })}
        {_.map(privateRoutes, (route, key) => {
          const { component, path } = route
          return (
            <Route
              exact
              path={path}
              key={key}
              render={r => (
                <Private component={component} route={r} />
              )}
            />
          )
        })}
        {_.map(sessionRoutes, (route, key) => {
          const { component, path } = route
          return (
            <Route
              exact
              path={path}
              key={key}
              render={r => <Public component={component} route={r} />}
            />
          )
        })}
        <Route path="*" component={NotFound} />
      </Switch>
    </Router>
  )
}

export default Template
