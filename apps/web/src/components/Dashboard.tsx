import React from 'react';

export const Dashboard: React.FC = () => {
  return (
    <div className="dashboard-container" style={{ padding: '24px', fontFamily: 'sans-serif' }}>
      <h1>ApexPay Enterprise Financial Operations</h1>
      <div className="metrics-grid" style={{ display: 'flex', gap: '16px', marginBottom: '24px' }}>
        <div className="card" style={{ padding: '16px', background: '#f4f6f8', borderRadius: '8px', flex: 1 }}>
          <h3>Total Ledger Volume</h3>
          <h2>$14,250,890.00</h2>
        </div>
        <div className="card" style={{ padding: '16px', background: '#f4f6f8', borderRadius: '8px', flex: 1 }}>
          <h3>Settled Payments (24h)</h3>
          <h2>1,420 Transactions</h2>
        </div>
        <div className="card" style={{ padding: '16px', background: '#f4f6f8', borderRadius: '8px', flex: 1 }}>
          <h3>Sanction Screening</h3>
          <h2>0 Unresolved Hits</h2>
        </div>
      </div>
    </div>
  );
};
