import axios from 'axios'
import jwtDecode from 'jwt-decode'

import { GetUser } from '../constants/user.constant'

export const getUserRequest = () => {
  return {
    type: GetUser.REQUEST
  }
}

export const getUserSuccess = response => {
  return {
    type: GetUser.SUCCESS,
    payload: {
      username: response.data.username,
      email: response.data.email,
      isActive: response.data.is_active,
      isAdmin: response.data.is_admin,
      isUser: response.is_user
    }
  }
}

export const getUserFailure = error => {
  return {
    type: GetUser.FAILURE,
    payload: {
      status: error.status,
      statusText: error.statusText
    }
  }
}

export const getUser = token => {
  const request = {
    method: 'get',
    url: `http://localhost/api/users/${jwtDecode(token).identity}`,
    headers: {
      Authorization: `Bearer ${token}`
    }
  }

  return dispatch => {
    dispatch(getUserRequest())
    return axios(request)
      .then(response => {
        if (response.status === 200) {
          dispatch(getUserSuccess(response.data))
        } else {
          dispatch(
            getUserFailure({
              response: {
                status: response.status,
                statusText: response.msg
              }
            })
          )
        }
      })
      .catch(err => {
        dispatch(getUserFailure(err))
      })
  }
}
