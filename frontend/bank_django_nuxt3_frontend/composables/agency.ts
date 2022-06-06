import AgencyRepositoryApi from "~~/repositories/agency_repository"
import Agency from "~~/types/agency"
import AgencyErrors from "~~/types/agencyErrors"

export function useAgency () {

  const agencies = useState<Agency[]>('agencies', () => [])
  const loading = useState<boolean>('loadingAgency', () => false)
  const agencyErrors = useState<AgencyErrors>('agencyErrors', () => {
    return {
      name: null,
      bank: null,
      agency_code: null
    }
  })
  const agency = useState<Agency>('agency', () => null)

  const getAgencies = async ():Promise<void> => {
    loading.value = true
    await AgencyRepositoryApi.all().then((response) => {
      agencies.value = response
    }).finally(() => {
      loading.value = false
    })
  }

  const getAgency = async (id:number):Promise<void> => {
    loading.value = true
    await AgencyRepositoryApi.get(id).then((response) => {
      agency.value = response
    }).finally(() => {
      loading.value = false
    })
  }

  const addAgency = async (params:any):Promise<any> => {
    loading.value = true
    return await AgencyRepositoryApi.add(params).then((response:any) => {
      clearErrors()
      return Promise.resolve(response)
    }).catch((errors:any) => {
      Object.keys(errors.data).forEach((value) => {
        errors.data[value] = errors.data[value].toString()
      })
      agencyErrors.value = errors.data
      return Promise.reject(errors)
    }).finally(() => {
      loading.value = false
    })
  }

  const editAgency = async (params:any):Promise<any> => {
    loading.value = true
    return await AgencyRepositoryApi.update(params).then((response:any) => {
      clearErrors()
      return Promise.resolve(response)
    }).catch((errors:any) => {
      Object.keys(errors.data).forEach((value) => {
        errors.data[value] = errors.data[value].toString()
      })
      agencyErrors.value = errors.data
      return Promise.reject(errors)
    }).finally(() => {
      loading.value = false
    })
  }

  const deleteAgency = async(bankId:number):Promise<any> => {
    loading.value = true
    return await AgencyRepositoryApi.delete(bankId).then(() => {
      getAgencies()
    }).finally(() => {
      loading.value = false
    })
  }

  const clearErrors = ():void => {
    agencyErrors.value = {
      name: null,
      bank: null,
      agency_code: null
    }
  }

  const clearAgency = ():void => {
    agency.value = null
  }

  const clearAgencies = ():void => {
    agencies.value = []
  }

  return {
    addAgency,
    deleteAgency,
    editAgency,
    getAgencies,
    getAgency,
    clearErrors,
    clearAgency,
    clearAgencies,
    agencies,
    agency,
    agencyErrors,
    loading
  }
}