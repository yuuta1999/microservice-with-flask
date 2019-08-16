import React from 'react'
import PropTypes from 'prop-types'
import { Link } from 'react-router-dom'
import {
  Nav,
  Navbar,
  NavDropdown,
  Container,
  Button,
  Row,
  Col
} from 'react-bootstrap'

import { history } from '../utils/misc'

class MyNavbar extends React.Component {
  constructor(props) {
    super(props)

    this.gotoRoute = this.gotoRoute.bind(this)
  }

  gotoRoute = route => {
    history.push(route)
  }

  logOut = event => {
    const { logout } = this.props
    event.preventDefault()
    logout()
    window.location.reload()
  }

  componentDidMount = () => {
    const { getUser } = this.props
    const token = localStorage.getItem('access_token')
    if (token) {
      getUser(token)
    }
  }

  render() {
    const { isAuthenticated } = this.props
    console.log(isAuthenticated)
    return (
      <header>
        <Navbar className="shadow" bg="light" expand="lg" fixed="top">
          <Container>
            <Navbar.Brand as={Link} to="/">
              React-Bootstrap
            </Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
              <Nav className="ml-auto">
                {isAuthenticated ? (
                  <>
                    <Nav.Link as={Link} to="/about">
                      About
                    </Nav.Link>
                    <NavDropdown alignRight id="basic-nav-dropdown">
                      <NavDropdown.Item href="/me">
                        Myself
                      </NavDropdown.Item>
                      <NavDropdown.Item href="/settings">
                        Profile
                      </NavDropdown.Item>
                      <NavDropdown.Divider />
                      <NavDropdown.Item
                        as={Button}
                        onClick={e => {
                          this.logOut(e)
                        }}
                      >
                        Logout
                      </NavDropdown.Item>
                    </NavDropdown>
                  </>
                ) : (
                  <Row>
                    <Col className="px-3">
                      <Button
                        variant="light"
                        onClick={() => this.gotoRoute('/about')}
                      >
                        About
                      </Button>
                    </Col>
                    <Col className="px-3">
                      <Button
                        variant="light"
                        onClick={() => this.gotoRoute('/register')}
                      >
                        Register
                      </Button>
                    </Col>
                    <Col className="px-3">
                      <Button
                        variant="dark"
                        onClick={() => this.gotoRoute('/login')}
                      >
                        Login
                      </Button>
                    </Col>
                  </Row>
                )}
              </Nav>
            </Navbar.Collapse>
          </Container>
        </Navbar>
      </header>
    )
  }
}

MyNavbar.propTypes = {
  isAuthenticated: PropTypes.bool.isRequired,
  getUser: PropTypes.func.isRequired,
  logout: PropTypes.func.isRequired
}

export default MyNavbar
