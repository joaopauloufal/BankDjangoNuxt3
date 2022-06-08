import ClientRepositoryApi from "~~/repositories/client_repository"
import Client from "~~/types/client"
import ClientErrors from "~~/types/clientErrors"

export function useClient () {

  const clients = useState<Client[]>('clients', () => [])
  const loading = useState<boolean>('loadingClient', () => false)
  const clientErrors = useState<ClientErrors>('clientErrors', () => {
    return {
      name: null,
      cpf_cnpj: null,
    }
  })
  const client = useState<Client>('client', () => null)

  const getClients = async ():Promise<void> => {
    loading.value = true
    await ClientRepositoryApi.all().then((response) => {
      clients.value = response
    }).finally(() => {
      loading.value = false
    })
  }

  const getClient = async (id:number):Promise<void> => {
    loading.value = true
    await ClientRepositoryApi.get(id).then((response) => {
      client.value = response
    }).finally(() => {
      loading.value = false
    })
  }

  const addClient = async (params:any):Promise<any> => {
    loading.value = true
    return await ClientRepositoryApi.add(params).then((response:any) => {
      clearErrors()
      return Promise.resolve(response)
    }).catch((errors:any) => {
      Object.keys(errors.data).forEach((value) => {
        errors.data[value] = errors.data[value].toString()
      })
      clientErrors.value = errors.data
      return Promise.reject(errors)
    }).finally(() => {
      loading.value = false
    })
  }

  const editClient = async (params:any):Promise<any> => {
    loading.value = true
    return await ClientRepositoryApi.update(params).then((response:any) => {
      clearErrors()
      return Promise.resolve(response)
    }).catch((errors:any) => {
      Object.keys(errors.data).forEach((value) => {
        errors.data[value] = errors.data[value].toString()
      })
      clientErrors.value = errors.data
      return Promise.reject(errors)
    }).finally(() => {
      loading.value = false
    })
  }

  const deleteClient = async(bankId:number):Promise<any> => {
    loading.value = true
    return await ClientRepositoryApi.delete(bankId).then(() => {
      getClients()
    }).finally(() => {
      loading.value = false
    })
  }

  const clearErrors = ():void => {
    clientErrors.value = {
      name: null,
      cpf_cnpj: null
    }
  }

  const clearClient = ():void => {
    client.value = null
  }

  const clearClients = ():void => {
    clients.value = []
  }

  return {
    addClient,
    deleteClient,
    editClient,
    getClients,
    getClient,
    clearErrors,
    clearClient,
    clearClients,
    clients,
    client,
    clientErrors,
    loading
  }
}