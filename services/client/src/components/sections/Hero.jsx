import React from 'react'
import PropTypes from 'prop-types'

import { Container, Row, Col } from 'react-bootstrap'

const Hero = props => {
  const { username, isAuthenticated } = props
  return (
    <>
      <div className="position-relative">
        <section className="section section-lg section-hero">
          <Container className="hero-container d-flex align-items-center py-lg">
            <div className="col px-0">
              <Row className="align-items-center justify-content-center">
                <Col className="text-center" lg="6">
                  <p className="lead text-black">
                    Hello&nbsp;
                    {isAuthenticated ? username : 'friend'}
                  </p>
                </Col>
              </Row>
            </div>
          </Container>
        </section>
      </div>
    </>
  )
}

Hero.propTypes = {
  username: PropTypes.string.isRequired,
  isAuthenticated: PropTypes.bool.isRequired
}

export default Hero
