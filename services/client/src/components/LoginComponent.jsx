import React from 'react'
import PropTypes from 'prop-types'
import {
  Card,
  Container,
  Button,
  Form,
  FormGroup,
  InputGroup
} from 'react-bootstrap'
import Octicon, { Person, Lock } from '@primer/octicons-react'

class LoginComponent extends React.Component {
  constructor(props) {
    super(props)

    this.state = {
      disabled: true,
      username: '',
      password: ''
    }
  }

  handleChange = (event, type) => {
    const { value } = event.target
    const nextState = {}
    nextState[type] = value
    this.setState(nextState, () => {
      this.disableBtn()
    })
  }

  handleSubmit = event => {
    const { disabled } = this.state
    if (event.key === 'Enter' || !disabled) {
      this.loginUser(event)
    }
  }

  loginUser = event => {
    const { login } = this.props
    const { username, password } = this.state
    event.preventDefault()
    login(username, password)
  }

  logOut = event => {
    const { logout } = this.props
    event.preventDefault()
    logout()
    window.location.reload()
  }

  disableBtn = () => {
    const { username, password } = this.state
    if (username !== '' && password !== '') {
      this.setState({
        disabled: false
      })
    }
  }

  componentDidMount = () => {
    const { getUser } = this.props
    const token = localStorage.getItem('access_token')
    if (token) {
      getUser(token)
    }
  }

  render = () => {
    const { username, password, disabled } = this.state
    const { isAuthenticated } = this.props
    return (
      <main>
        <div className="position-relative">
          <section className="section section-lg section-hero">
            <Container className="login-container">
              <Card bg="light" className="align-items-center">
                {!isAuthenticated ? (
                  <Card.Body as="article" className="mx-auto">
                    <Card.Title as="h4" className="mt-3 text-center">
                      Login
                    </Card.Title>
                    <Button className="btn-facebook" block>
                      Login with Facebook
                    </Button>
                    <Button className="btn-google" block>
                      Login with Google
                    </Button>
                    <p className="divider-text">
                      <span className="bg-light">OR</span>
                    </p>
                    <Form>
                      <FormGroup controlId="validateUsernameForm">
                        <InputGroup>
                          <InputGroup.Prepend>
                            <InputGroup.Text id="inputGroupPrependUsername">
                              <Octicon icon={Person} />
                            </InputGroup.Text>
                          </InputGroup.Prepend>
                          <Form.Control
                            type="text"
                            placeholder="Username"
                            aria-describedby="inputGroupPrependUsername"
                            name="username"
                            value={username}
                            onChange={e =>
                              this.handleChange(e, 'username')
                            }
                          />
                        </InputGroup>
                      </FormGroup>
                      <FormGroup controlId="validatePasswordForm">
                        <InputGroup>
                          <InputGroup.Prepend>
                            <InputGroup.Text id="inputGroupPrependPassword">
                              <Octicon icon={Lock} />
                            </InputGroup.Text>
                          </InputGroup.Prepend>
                          <Form.Control
                            type="password"
                            placeholder="Password"
                            aria-describedby="inputGroupPrependPassword"
                            name="password"
                            value={password}
                            onChange={e =>
                              this.handleChange(e, 'password')
                            }
                          />
                        </InputGroup>
                      </FormGroup>
                      <FormGroup>
                        <Button
                          type="submit"
                          disabled={disabled}
                          block
                          onClick={e => this.loginUser(e)}
                        >
                          Login
                        </Button>
                      </FormGroup>
                    </Form>
                  </Card.Body>
                ) : (
                  <Card.Body as="article" className="mx-auto">
                    <Card.Title as="h4" className="mt-3 text-center">
                      Wanna log out?
                    </Card.Title>
                    <Button
                      className="mx-auto"
                      variant="secondary"
                      onClick={e => {
                        this.logOut(e)
                      }}
                    >
                      Logout
                    </Button>
                  </Card.Body>
                )}
              </Card>
            </Container>
          </section>
        </div>
      </main>
    )
  }
}

LoginComponent.propTypes = {
  login: PropTypes.func.isRequired,
  getUser: PropTypes.func.isRequired,
  isAuthenticated: PropTypes.bool.isRequired,
  logout: PropTypes.func.isRequired
}

export default LoginComponent
