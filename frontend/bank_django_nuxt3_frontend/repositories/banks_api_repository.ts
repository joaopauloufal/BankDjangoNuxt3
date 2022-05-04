import client from './api_repository'

export default {
  all() {
    return client.get(`banks/`)
  }
}