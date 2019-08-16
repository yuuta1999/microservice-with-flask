import axios from 'axios'

import { history } from '../utils/misc'
import { Login, Logout } from '../constants/login.constant'

export const loginRequest = () => {
  return {
    type: Login.REQUEST
  }
}

export const loginSuccess = token => {
  localStorage.setItem('access_token', token)
  return {
    type: Login.SUCCESS,
    payload: {
      access_token: token
    }
  }
}

export const loginFailure = error => {
  return {
    type: Login.FAILURE,
    payload: {
      status: error.status,
      statusText: error.statusText
    }
  }
}

export const login = (username, password) => {
  const request = {
    method: 'post',
    url: 'http://localhost/api/login',
    headers: {
      'Content-Type': 'application/json'
    },
    data: {
      username,
      password
    }
  }

  return dispatch => {
    dispatch(loginRequest())
    return axios(request)
      .then(response => {
        try {
          dispatch(loginSuccess(response.data.access_token))
          history.push('/')
        } catch (e) {
          dispatch(
            loginFailure({
              response: {
                status: 403,
                statusText: 'Invalid token.'
              }
            })
          )
        }
      })
      .catch(e => {
        dispatch(loginFailure(e))
      })
  }
}

export const logout = () => {
  localStorage.removeItem('access_token')
  return {
    type: Logout.REQUEST,
    payload: {
      statusText: 'Logout successfully'
    }
  }
}
