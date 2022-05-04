import Bank from "~~/types/bank";

export const getBanks = () => useState<Bank[]>('banks', () => {
  return []
  
})