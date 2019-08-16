import { createBrowserHistory } from 'history'

export const history = createBrowserHistory()

/**
 * Take a list of initial states and a map of
 * actions, return a map of reduced states.
 *
 * @param {*} initialState
 * @param {*} reducerMap
 */
export const createReducer = (initialState, reducerMap) => {
  // Means function ...(state=initialState, action) {...}
  return (state = initialState, action) => {
    // switch (action.type) { ... (When the action matches the constant) }
    const reducer = reducerMap[action.type]

    // When matched, return an object of reduced state.
    // Default is state.
    return reducer ? reducer(state, action.payload) : state
  }
}
