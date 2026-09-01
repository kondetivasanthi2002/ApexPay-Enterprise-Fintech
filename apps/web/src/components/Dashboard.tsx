import React, { useState } from 'react';
import { 
  ShieldCheck, 
  CreditCard, 
  BookOpen, 
  BarChart3, 
  TrendingUp, 
  AlertTriangle, 
  ArrowUpRight, 
  CheckCircle2, 
  Zap, 
  DollarSign, 
  RefreshCw 
} from 'lucide-react';

export const Dashboard: React.FC = () => {
  const [activeTab, setActiveTab] = useState<'overview' | 'ledger' | 'payments' | 'compliance' | 'credit' | 'trading'>('overview');

  return (
    <div style={{ fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif', backgroundColor: '#0f172a', color: '#f8fafc', minHeight: '100vh', padding: '24px' }}>
      
      {/* Top Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '24px', borderBottom: '1px solid #1e293b', paddingBottom: '16px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <div style={{ width: '40px', height: '40px', borderRadius: '12px', background: 'linear-gradient(135deg, #6366f1, #10b981)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
            <ShieldCheck size={24} color="#ffffff" />
          </div>
          <div>
            <h1 style={{ margin: 0, fontSize: '22px', fontWeight: 700 }}>ApexPay <span style={{ fontSize: '11px', background: 'rgba(16,185,129,0.2)', color: '#10b981', padding: '2px 8px', borderRadius: '12px', textTransform: 'uppercase' }}>Enterprise</span></h1>
            <p style={{ margin: 0, fontSize: '12px', color: '#94a3b8' }}>Core Banking Ledger & Money Movement Engine</p>
          </div>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <span style={{ display: 'inline-flex', alignItems: 'center', gap: '6px', fontSize: '12px', background: 'rgba(16,185,129,0.15)', color: '#10b981', padding: '6px 12px', borderRadius: '20px', fontWeight: 600 }}>
            <span style={{ width: '8px', height: '8px', borderRadius: '50%', backgroundColor: '#10b981' }}></span>
            System Online • v1.0.0
          </span>
        </div>
      </div>

      {/* Navigation Icons Bar */}
      <div style={{ display: 'flex', gap: '8px', marginBottom: '24px', background: '#1e293b', padding: '6px', borderRadius: '12px' }}>
        {[
          { id: 'overview', label: 'Overview', icon: BarChart3 },
          { id: 'ledger', label: 'Double-Entry Ledger', icon: BookOpen },
          { id: 'payments', label: 'Payments Gateway', icon: CreditCard },
          { id: 'compliance', label: 'KYC & Sanctions', icon: ShieldCheck },
          { id: 'credit', label: 'Credit Risk', icon: TrendingUp },
          { id: 'trading', label: 'Order Engine', icon: Zap }
        ].map(tab => {
          const IconComponent = tab.icon;
          const isActive = activeTab === tab.id;
          return (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id as any)}
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: '8px',
                padding: '10px 16px',
                borderRadius: '8px',
                border: 'none',
                cursor: 'pointer',
                fontWeight: 600,
                fontSize: '13px',
                backgroundColor: isActive ? '#6366f1' : 'transparent',
                color: isActive ? '#ffffff' : '#94a3b8',
                transition: 'all 0.2s'
              }}
            >
              <IconComponent size={16} />
              {tab.label}
            </button>
          );
        })}
      </div>

      {/* Metrics Cards Grid */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '16px', marginBottom: '24px' }}>
        <div style={{ background: '#1e293b', padding: '16px', borderRadius: '12px', border: '1px solid #334155' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', color: '#94a3b8', fontSize: '11px', fontWeight: 600, textTransform: 'uppercase' }}>
            <span>24h Transaction Volume</span>
            <DollarSign size={16} color="#10b981" />
          </div>
          <h2 style={{ margin: '8px 0', fontSize: '24px' }}>$14,250,890.00</h2>
          <span style={{ fontSize: '12px', color: '#10b981', display: 'flex', alignItems: 'center', gap: '4px' }}>
            <ArrowUpRight size={14} /> +14.2% from yesterday
          </span>
        </div>

        <div style={{ background: '#1e293b', padding: '16px', borderRadius: '12px', border: '1px solid #334155' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', color: '#94a3b8', fontSize: '11px', fontWeight: 600, textTransform: 'uppercase' }}>
            <span>Settlement Rate</span>
            <CheckCircle2 size={16} color="#6366f1" />
          </div>
          <h2 style={{ margin: '8px 0', fontSize: '24px' }}>99.98%</h2>
          <span style={{ fontSize: '12px', color: '#94a3b8' }}>1,420 Settled ACH/Wires</span>
        </div>

        <div style={{ background: '#1e293b', padding: '16px', borderRadius: '12px', border: '1px solid #334155' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', color: '#94a3b8', fontSize: '11px', fontWeight: 600, textTransform: 'uppercase' }}>
            <span>OFAC Sanction Hits</span>
            <ShieldCheck size={16} color="#10b981" />
          </div>
          <h2 style={{ margin: '8px 0', fontSize: '24px' }}>0 <span style={{ fontSize: '11px', background: 'rgba(16,185,129,0.2)', color: '#10b981', padding: '2px 8px', borderRadius: '12px' }}>Compliant</span></h2>
          <span style={{ fontSize: '12px', color: '#94a3b8' }}>Fuzzy Match Score: 0.70</span>
        </div>

        <div style={{ background: '#1e293b', padding: '16px', borderRadius: '12px', border: '1px solid #334155' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', color: '#94a3b8', fontSize: '11px', fontWeight: 600, textTransform: 'uppercase' }}>
            <span>Loan Portfolio Value</span>
            <TrendingUp size={16} color="#f59e0b" />
          </div>
          <h2 style={{ margin: '8px 0', fontSize: '24px' }}>$4,850,000.00</h2>
          <span style={{ fontSize: '12px', color: '#94a3b8' }}>Avg Portfolio FICO: 742</span>
        </div>
      </div>

    </div>
  );
};
