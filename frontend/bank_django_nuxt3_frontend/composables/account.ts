import AccountRepositoryApi from "~~/repositories/account_repository"
import Account from "~~/types/account"
import AccountErrors from "~~/types/accountErrors"

export function useAccount () {

  const accounts = useState<Account[]>('accounts', () => [])
  const loading = useState<boolean>('loadingAccount', () => false)
  const accountErrors = useState<AccountErrors>('accountErrors', () => {
    return {
      number: null,
      type: null,
      client: null,
      balance: null,
      agency: null
    }
  })
  const account = useState<Account>('account', () => null)

  const getAccounts = async ():Promise<void> => {
    loading.value = true
    await AccountRepositoryApi.all().then((response) => {
      accounts.value = response
    }).finally(() => {
      loading.value = false
    })
  }

  const getAccount = async (id:number):Promise<void> => {
    loading.value = true
    await AccountRepositoryApi.get(id).then((response) => {
      account.value = response
    }).finally(() => {
      loading.value = false
    })
  }

  const addAccount = async (params:any):Promise<any> => {
    loading.value = true
    return await AccountRepositoryApi.add(params).then((response:any) => {
      clearErrors()
      return Promise.resolve(response)
    }).catch((errors:any) => {
      Object.keys(errors.data).forEach((value) => {
        errors.data[value] = errors.data[value].toString()
      })
      accountErrors.value = errors.data
      return Promise.reject(errors)
    }).finally(() => {
      loading.value = false
    })
  }

  const editAccount = async (params:any):Promise<any> => {
    loading.value = true
    return await AccountRepositoryApi.update(params).then((response:any) => {
      clearErrors()
      return Promise.resolve(response)
    }).catch((errors:any) => {
      Object.keys(errors.data).forEach((value) => {
        errors.data[value] = errors.data[value].toString()
      })
      accountErrors.value = errors.data
      return Promise.reject(errors)
    }).finally(() => {
      loading.value = false
    })
  }

  const deleteAccount = async(bankId:number):Promise<any> => {
    loading.value = true
    return await AccountRepositoryApi.delete(bankId).then(() => {
      getAccounts()
    }).finally(() => {
      loading.value = false
    })
  }

  const clearErrors = ():void => {
    accountErrors.value = {
      number: null,
      type: null,
      client: null,
      balance: null,
      agency: null
    }
  }

  const clearAccount = ():void => {
    account.value = null
  }

  const clearAccounts = ():void => {
    accounts.value = []
  }

  return {
    addAccount,
    deleteAccount,
    editAccount,
    getAccounts,
    getAccount,
    clearErrors,
    clearAccount,
    clearAccounts,
    accounts,
    account,
    accountErrors,
    loading
  }
}