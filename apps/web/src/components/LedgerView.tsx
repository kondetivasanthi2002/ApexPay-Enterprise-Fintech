import React from 'react';
import { Account } from '../types';

interface LedgerViewProps {
  accounts: Account[];
}

export const LedgerView: React.FC<LedgerViewProps> = ({ accounts }) => {
  return (
    <div className="ledger-table-container">
      <h2>General Ledger Chart of Accounts</h2>
      <table style={{ width: '100%', borderCollapse: 'collapse' }}>
        <thead>
          <tr style={{ background: '#0f172a', color: '#ffffff' }}>
            <th style={{ padding: '8px' }}>Account ID</th>
            <th style={{ padding: '8px' }}>Name</th>
            <th style={{ padding: '8px' }}>Type</th>
            <th style={{ padding: '8px' }}>Balance</th>
          </tr>
        </thead>
        <tbody>
          {accounts.map(acc => (
            <tr key={acc.account_id} style={{ borderBottom: '1px solid #e2e8f0' }}>
              <td style={{ padding: '8px' }}>{acc.account_id}</td>
              <td style={{ padding: '8px' }}>{acc.name}</td>
              <td style={{ padding: '8px' }}>{acc.account_type}</td>
              <td style={{ padding: '8px' }}>{acc.currency} ${acc.balance}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};
