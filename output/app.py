import streamlit as st
import trading_simulation_platform as tsp

def main():
    st.title('Trading Simulation Platform')

    # Authentication Section
    st.sidebar.header('User Authentication')
    auth_mode = st.sidebar.radio('Select Mode', ['Login', 'Sign Up'])
    username = st.sidebar.text_input('Username')
    password = st.sidebar.text_input('Password', type='password')

    user_system = tsp.User()

    if auth_mode == 'Sign Up':
        if st.sidebar.button('Sign Up'):
            if user_system.sign_up(username, password):
                st.sidebar.success('Successfully signed up!')
            else:
                st.sidebar.error('Username already exists')

    if auth_mode == 'Login':
        if st.sidebar.button('Login'):
            if user_system.login(username, password):
                st.sidebar.success('Login Successful!')
                show_dashboard(username)
            else:
                st.sidebar.error('Invalid credentials')

def show_dashboard(username):
    # Virtual Wallet Section
    st.header(f'Welcome, {username}!')
    wallet = tsp.VirtualWallet()
    
    st.subheader('Virtual Wallet')
    funds = st.number_input('Add Funds', min_value=0.0, step=100.0)
    if st.button('Add to Wallet'):
        wallet.add_funds(funds)
        st.success(f'Added ${funds}. Current Balance: ${wallet.check_balance()}')

    # Trading Section
    st.subheader('Trading')
    trade_system = tsp.Trade()
    
    asset_types = ['BTC', 'ETH', 'AAPL']
    asset = st.selectbox('Select Asset', asset_types)
    
    current_price = trade_system.view_current_price(asset)
    st.write(f'Current {asset} Price: ${current_price}')
    
    trade_amount = st.number_input(f'Trade Amount of {asset}', min_value=0.0, step=0.1)
    
    if st.button('Execute Trade'):
        if trade_system.execute_trade(asset, trade_amount):
            st.success(f'Trade executed: {trade_amount} {asset}')
        else:
            st.error('Trade execution failed')

    # Portfolio Section
    st.subheader('Portfolio')
    portfolio = tsp.Portfolio()
    st.write(f'Portfolio Balance: ${portfolio.get_balance()}')
    
    st.write('Trade History:')
    trade_history = portfolio.view_trade_history()
    if trade_history:
        for trade in trade_history:
            st.write(trade)
    else:
        st.write('No trades yet')

if __name__ == '__main__':
    main()