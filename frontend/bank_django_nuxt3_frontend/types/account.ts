import Agency from "./agency"
import Client from "./client"

enum AccountType {
  Physical = 'PHYSICAL',
  Legal = 'LEGAL'
}

interface Account {
  number: string,
  type: AccountType,
  client: Client,
  balance: number
  agency: Agency
}

export default Account