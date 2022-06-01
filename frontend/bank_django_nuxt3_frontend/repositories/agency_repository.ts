import ApiRepository from '~~/repositories/api_repository'
import Agency from '~~/types/agency'

export default class AgencyRepositoryApi {

  static all():Promise<Agency[]> {
    return ApiRepository.get(`agencies/`)
  }

  static get(id:number):Promise<Agency> {
    return ApiRepository.get(`agencies/${id}/`)
  }

  static add(params:any):Promise<any> {
    return ApiRepository.post(`agencies/`, params)
  }

  static delete(id:number):Promise<any> {
    return ApiRepository.delete(`agencies/${id}/`)
  }

  static update(params:any):Promise<any> {
    return ApiRepository.put(`agencies/${params.id}/`, params)
  }

}
