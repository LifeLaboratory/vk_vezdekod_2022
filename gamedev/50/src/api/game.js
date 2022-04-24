const axios = require('axios')

export function getGame (session) {
  return axios.get(`http://79.141.74.176:13454/api/game/`,
    {
      headers: {
        session: session
      }
    })
    .then(function (response) {
      return response.data
    })
    .catch(function (error) {
      console.log(error)
      return false
    })
}

export function newGame (session, id) {
  return axios.post(`http://79.141.74.176:13454/api/game/`,
    JSON.stringify( {"id_person": id} ),
    {
      headers: {
        session: session,
        'Content-Type': 'application/json'
      }
    })
    .then(function (response) {
      return response.data
    })
    .catch(function (error) {
      console.log(error)
      return false
    })
}

export function sendAnswer (session, ans) {
  return axios.post(`http://79.141.74.176:13454/api/game/question/`,
    JSON.stringify( {answer: ans} ),
    {
      headers: {
        session: session,
        'Content-Type': 'application/json'
      }
    })
    .then(function (response) {
      return response.data
    })
    .catch(function (error) {
      console.log(error)
      return false
    })
}

export function resumeGame (session) {
  return axios.get(`http://79.141.74.176:13454/api/game/`,
    {
      headers: {
        session: session,
      }
    })
    .then(function (response) {
      return response.data
    })
    .catch(function (error) {
      console.log(error)
      return false
    })
}