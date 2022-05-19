import ApiRepository from '~~/repositories/api_repository'
import Bank from '~~/types/bank'

export default class BankRepositoryApi {

  static all():Promise<Bank[]> {
    return ApiRepository.get(`banks/`)
  }

  static add(params:any):any {
    return ApiRepository.post(`banks/`, params)
  }

}
