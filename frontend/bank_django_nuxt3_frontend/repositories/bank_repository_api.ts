import ApiRepository from '~~/repositories/api_repository'
import Bank from '~~/types/bank'

export default class BankRepositoryApi {

  static all():Promise<Bank[]> {
    return ApiRepository.get(`banks/`)
  }

  static get(id:number):Promise<Bank> {
    return ApiRepository.get(`banks/${id}/`)
  }

  static add(params:any):Promise<any> {
    return ApiRepository.post(`banks/`, params)
  }

  static delete(bankId:number):Promise<any> {
    return ApiRepository.delete(`banks/${bankId}/`)
  }

  static update(params:any):Promise<any> {
    return ApiRepository.put(`banks/${params.id}/`, params)
  }

}
