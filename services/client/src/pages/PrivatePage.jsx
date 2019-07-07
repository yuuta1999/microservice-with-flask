import React from 'react'
import PropTypes from 'prop-types'

const PrivatePage = props => {
  const { component: Component, route } = props
  console.log(route)
  return (
    <div>
      <Component route={route} />
    </div>
  )
}

PrivatePage.propTypes = {
  component: PropTypes.func.isRequired,
  route: PropTypes.shape({
    history: PropTypes.object,
    location: PropTypes.object,
    match: PropTypes.object
  }).isRequired
}

export default PrivatePage
