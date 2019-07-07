import React from 'react'
import PropTypes from 'prop-types'

import Header from '../containers/HeaderContainer'
import Footer from '../containers/FooterContainer'

const PublicPage = props => {
  const { component: Component, route } = props
  console.log(props)
  return (
    <div>
      <Header />
      <Component route={route} />
      <Footer />
    </div>
  )
}

PublicPage.propTypes = {
  component: PropTypes.func.isRequired,
  route: PropTypes.shape({
    history: PropTypes.object,
    location: PropTypes.object,
    match: PropTypes.object
  }).isRequired
}

export default PublicPage
