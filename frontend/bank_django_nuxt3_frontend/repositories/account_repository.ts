import ApiRepository from '~~/repositories/api_repository'
import Account from '~~/types/account'

export default class AccountRepositoryApi {

  static all():Promise<Account[]> {
    return ApiRepository.get(`accounts/`)
  }

  static get(id:number):Promise<Account> {
    return ApiRepository.get(`accounts/${id}/`)
  }

  static add(params:any):Promise<any> {
    return ApiRepository.post(`accounts/`, params)
  }

  static delete(id:number):Promise<any> {
    return ApiRepository.delete(`accounts/${id}/`)
  }

  static update(params:any):Promise<any> {
    return ApiRepository.put(`accounts/${params.id}/`, params)
  }

  static deposit(params:any):Promise<any> {
    return ApiRepository.put(`accounts/${params.id}/deposit/`, params)
  }

  static withdraw(params:any):Promise<any> {
    return ApiRepository.put(`accounts/${params.id}/withdraw/`, params)
  }

}
