import Bank from "./bank"

interface Agency {
  id: number,
  agency_code: string,
  bank: Bank,
  name: string
}

export default Agency