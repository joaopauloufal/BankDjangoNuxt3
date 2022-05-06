import Bank from "types/bank"
import BankRepositoryApi  from '~~/repositories/bank_repository_api'

export const getBanks = () => useState<Bank[]>('banks', () => {
  const { data } = useAsyncData('data', async () =>  await BankRepositoryApi.all())
  return data
})