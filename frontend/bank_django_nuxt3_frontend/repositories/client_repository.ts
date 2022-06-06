import ApiRepository from '~~/repositories/api_repository'
import Client from '~~/types/client'

export default class ClientRepositoryApi {

  static all():Promise<Client[]> {
    return ApiRepository.get(`clients/`)
  }

  static get(id:number):Promise<Client> {
    return ApiRepository.get(`clients/${id}/`)
  }

  static add(params:any):Promise<any> {
    return ApiRepository.post(`clients/`, params)
  }

  static delete(id:number):Promise<any> {
    return ApiRepository.delete(`clients/${id}/`)
  }

  static update(params:any):Promise<any> {
    return ApiRepository.put(`clients/${params.id}/`, params)
  }

}
