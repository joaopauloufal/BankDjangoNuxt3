import { $fetch } from 'ohmyfetch'
import { NotificationProgrammatic } from '@oruga-ui/oruga-next'

const options:object = {
  baseURL: '/api/v1/',
}

const client = $fetch.create(options)

export default {

  async get(url:string):Promise<any> {
    return client(url)
  },

  async post(url:string, data:object):Promise<any> {
    return client(url, { method: 'POST', body: data })
      .then(response => Promise.resolve(response))
      .catch((error) => {
          if (error.response.status === 400) {
              NotificationProgrammatic.open({
                  message: error.response.data.message,
                  variant: 'danger',
                  duration: 3000
              })
          }
        return Promise.reject(error)
      });
  },

  async put(url:string, data:object):Promise<any> {
    return client(url, { method: 'PUT', body: data })
      .then(response => Promise.resolve(response))
      .catch((error) => {
        if (error.response.status === 400) {
            NotificationProgrammatic.open({
                message: error.response.data.message,
                variant: 'danger',
                duration: 3000
            })
        }
      return Promise.reject(error)
    });
  },

  async delete(url:string):Promise<any> {
    return client(url, { method: 'DELETE' })
      .then(response => Promise.resolve(response))
      .catch((error) => {
        if (error.response.status === 400) {
          NotificationProgrammatic.open({
              message: error.response.data.message,
              variant: 'danger',
              duration: 3000
          })
        }
      return Promise.reject(error)
    });
  },
}