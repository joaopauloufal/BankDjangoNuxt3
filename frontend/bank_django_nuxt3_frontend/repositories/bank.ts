import ApiRepository from 'repositories/api_repository'

export default {

  all():Promise<any> {
    return ApiRepository.get(`banks/`)
  }

}