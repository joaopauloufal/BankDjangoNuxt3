import { $fetch } from 'ohmyfetch'
import { NotificationProgrammatic } from '@oruga-ui/oruga-next'

const options:object = {
  baseURL: 'http://localhost:8000/api/v1/',
}

const client = $fetch.create(options)

export default class ApiRepository {

  static async get(url:string):Promise<any> {
    return await client(url).then(response => Promise.resolve(response)).catch((error) => {
      NotificationProgrammatic.open({
        message: 'There was an error fetching the data. Please try again.',
        variant: 'danger',
        rootClass: 'toast-notification',
        position: 'top',
        duration: 3000,
      })
      return Promise.reject(error)
    })
  }

  static async post(url:string, data:object):Promise<any> {
    return await client(url, { method: 'POST', body: data })
      .then(response => Promise.resolve(response))
      .catch((error) => {
        if (error.response.status === 400) {
          NotificationProgrammatic.open({
            message: 'There are errors in the form. Please correct them before submitting again.',
            variant: 'danger',
            rootClass: 'toast-notification',
            position: 'top',
            duration: 3000,
          })
        }        
        return Promise.reject(error)
      });
  }

  static async put(url:string, data:object):Promise<any> {
    return client(url, { method: 'PUT', body: data })
      .then(response => Promise.resolve(response))
      .catch((error) => {
        if (error.response.status === 400) {
            NotificationProgrammatic.open({
                message: 'There are errors in the form. Please correct them before submitting again.',
                variant: 'danger',
                duration: 3000
            })
        }
      return Promise.reject(error)
    });
  }

  static async delete(url:string):Promise<any> {
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
  }
}