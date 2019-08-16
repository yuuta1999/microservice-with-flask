import React from 'react'
import PropTypes from 'prop-types'

import Hero from './sections/Hero'

class HomeComponent extends React.Component {
  componentDidMount = () => {
    const { getUser } = this.props
    const token = localStorage.getItem('access_token')
    if (token) {
      getUser(token)
    }
  }

  shouldComponentUpdate = nextProps => {
    const { username } = this.props
    return username !== nextProps.username
  }

  render() {
    return (
      <main>
        <Hero {...this.props} />
      </main>
    )
  }
}

HomeComponent.propTypes = {
  isAuthenticated: PropTypes.bool.isRequired,
  username: PropTypes.string.isRequired,
  getUser: PropTypes.func.isRequired
}

export default HomeComponent
