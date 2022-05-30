import BankRepositoryApi  from '~~/repositories/bank_repository_api'
import Bank from '~~/types/bank'
import BankErrors from '~~/types/bankErrors'

export function useBank (){

  const banks = useState<Bank[]>('banks', () => [])
  const loading = useState<boolean>('loadingBank', () => false)
  const bankErrors = useState<BankErrors>('bankErrors', () => {
    return {
      bank_code: null,
      name: null
    }
  })
  const bank = useState<Bank>('bank', () => null)

  const getBanks = async ():Promise<void> => {
    loading.value = true
    await BankRepositoryApi.all().then((response) => {
      banks.value = response
    }).finally(() => {
      loading.value = false
    })
  }

  const getBank = async (id:number):Promise<void> => {
    loading.value = true
    await BankRepositoryApi.get(id).then((response) => {
      bank.value = response
    }).finally(() => {
      loading.value = false
    })
  }

  const addBank = async (params:any):Promise<any> => {
    loading.value = true
    return await BankRepositoryApi.add(params).then((response:any) => {
      clearErrors()
      return Promise.resolve(response)
    }).catch((errors:any) => {
      Object.keys(errors.data).forEach((value) => {
        errors.data[value] = errors.data[value].toString()
      })
      bankErrors.value = errors.data
      return Promise.reject(errors)
    }).finally(() => {
      loading.value = false
    })
  }

  const editBank = async (params:any):Promise<any> => {
    loading.value = true
    return await BankRepositoryApi.update(params).then((response:any) => {
      clearErrors()
      return Promise.resolve(response)
    }).catch((errors:any) => {
      Object.keys(errors.data).forEach((value) => {
        errors.data[value] = errors.data[value].toString()
      })
      bankErrors.value = errors.data
      return Promise.reject(errors)
    }).finally(() => {
      loading.value = false
    })
  }

  const deleteBank = async(bankId:number):Promise<any> => {
    loading.value = true
    return await BankRepositoryApi.delete(bankId).then(() => {
      getBanks()
    }).finally(() => {
      loading.value = false
    })
  }

  const clearErrors = ():void => {
    bankErrors.value = {
      bank_code: null,
      name: null
    }
  }
  
  const clearBank = ():void => {
    bank.value = null
  }

  return {
    addBank,
    deleteBank,
    editBank,
    getBanks,
    getBank,
    clearErrors,
    clearBank,
    banks,
    bank,
    bankErrors,
    loading
  }
}