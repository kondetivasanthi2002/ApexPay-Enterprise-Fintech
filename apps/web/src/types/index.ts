export interface Account {
  account_id: string;
  account_number: string;
  name: string;
  account_type: 'ASSET' | 'LIABILITY' | 'EQUITY' | 'REVENUE' | 'EXPENSE';
  balance: string;
  currency: string;
}

export interface PaymentRequest {
  payment_id: string;
  amount: number;
  currency: string;
  method: 'ACH' | 'WIRE' | 'CARD';
}
