import pytest
import trading_simulation_platform as tsp
import datetime
import uuid

class TestSecurity:
    def test_encrypt_data(self):
        # Test data encryption
        test_data = "test_password"
        encrypted = tsp.Security.encrypt_data(test_data)
        assert isinstance(encrypted, str)
        assert len(encrypted) > 0
        assert encrypted == tsp.Security.encrypt_data(test_data)  # Consistent encryption

    def test_verify_user_identity(self):
        # Test user identity verification
        assert tsp.Security.verify_user_identity(123) is True
        assert tsp.Security.verify_user_identity(None) is False

class TestUser:
    def setup_method(self):
        self.user_system = tsp.User()

    def test_sign_up(self):
        # Test successful sign up
        assert self.user_system.sign_up('testuser', 'password123') is True
        
        # Test duplicate username prevention
        assert self.user_system.sign_up('testuser', 'another_password') is False

    def test_login(self):
        # Sign up first
        self.user_system.sign_up('loginuser', 'correct_password')
        
        # Test successful login
        assert self.user_system.login('loginuser', 'correct_password') is True
        
        # Test failed login
        assert self.user_system.login('loginuser', 'wrong_password') is False
        assert self.user_system.login('nonexistent', 'password') is False

class TestVirtualWallet:
    def setup_method(self):
        self.wallet = tsp.VirtualWallet()

    def test_initial_balance(self):
        # Test default initial balance
        assert self.wallet.balance == 0.0

    def test_add_funds(self):
        # Test adding positive funds
        self.wallet.add_funds(100.0)
        assert self.wallet.balance == 100.0

        # Test adding additional funds
        self.wallet.add_funds(50.0)
        assert self.wallet.balance == 150.0

        # Test adding zero or negative funds
        self.wallet.add_funds(0)
        self.wallet.add_funds(-10)
        assert self.wallet.balance == 150.0

    def test_check_balance(self):
        # Test balance checking
        assert self.wallet.check_balance() == 0.0
        self.wallet.add_funds(200.0)
        assert self.wallet.check_balance() == 200.0

class TestTrade:
    def setup_method(self):
        self.trade_system = tsp.Trade()

    def test_execute_trade(self):
        # Test successful trade execution
        assert self.trade_system.execute_trade('BTC', 0.5) is True
        assert len(self.trade_system.trades) == 1
        
        # Test trade details
        trade = self.trade_system.trades[0]
        assert trade['asset_type'] == 'BTC'
        assert trade['amount'] == 0.5
        assert isinstance(trade['timestamp'], datetime.datetime)

        # Test invalid trade amount
        assert self.trade_system.execute_trade('ETH', -1) is False

    def test_view_current_price(self):
        # Test price retrieval
        assert self.trade_system.view_current_price('BTC') == 50000.0
        assert self.trade_system.view_current_price('ETH') == 3000.0
        assert self.trade_system.view_current_price('AAPL') == 150.0
        assert self.trade_system.view_current_price('UNKNOWN') == 0.0

    def test_cancel_trade(self):
        # Execute a trade first
        self.trade_system.execute_trade('BTC', 0.5)
        first_trade_id = self.trade_system.trades[0]['trade_id']

        # Test successful trade cancellation
        assert self.trade_system.cancel_trade(first_trade_id) is True
        assert len(self.trade_system.trades) == 0

        # Test cancelling non-existent trade
        assert self.trade_system.cancel_trade(999) is False

class TestAPIIntegration:
    def setup_method(self):
        self.api = tsp.APIIntegration()

    def test_fetch_current_data(self):
        # Test data retrieval
        btc_data = self.api.fetch_current_data('BTC')
        assert btc_data == {'price': 50000.0, 'volume': 1000000}

        eth_data = self.api.fetch_current_data('ETH')
        assert eth_data == {'price': 3000.0, 'volume': 500000}

        # Test non-existent asset
        assert self.api.fetch_current_data('UNKNOWN') == {}

    def test_update_market_data(self):
        # Test market data update
        self.api.update_market_data('BTC')
        assert 'BTC' in self.api.market_data

class TestPortfolio:
    def setup_method(self):
        self.portfolio = tsp.Portfolio()

    def test_add_trade(self):
        # Test adding a trade
        test_trade = {'asset_type': 'BTC', 'amount': 0.5}
        self.portfolio.add_trade(test_trade)
        assert len(self.portfolio.trades) == 1
        assert self.portfolio.trades[0] == test_trade

    def test_get_balance(self):
        # Add some trades and funds
        test_trade1 = {'asset_type': 'BTC', 'amount': 100.0}
        test_trade2 = {'asset_type': 'ETH', 'amount': 50.0}
        
        self.portfolio.add_trade(test_trade1)
        self.portfolio.add_trade(test_trade2)
        
        self.portfolio.wallet.add_funds(200.0)

        # Check total balance
        assert self.portfolio.get_balance() == 350.0

    def test_view_trade_history(self):
        # Add trades
        test_trades = [
            {'asset_type': 'BTC', 'amount': 0.5},
            {'asset_type': 'ETH', 'amount': 1.0}
        ]
        
        for trade in test_trades:
            self.portfolio.add_trade(trade)

        # Check trade history
        history = self.portfolio.view_trade_history()
        assert len(history) == 2
        assert history == test_trades

# Optional: Main block for direct execution
if __name__ == '__main__':
    pytest.main([__file__])