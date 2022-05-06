import ApiRepository from '~~/repositories/api_repository'
import Bank from '~~/types/bank'

export default class BankRepositoryApi {

  static all():Promise<Bank[]> {
    return ApiRepository.get(`banks/`)
  }

}
