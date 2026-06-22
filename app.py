import streamlit as st

st.set_page_config(page_title="Online supermarket", layout="wide")
st.title("Online supermarket")

if "inventory" not in st.session_state:
    st.session_state.inventory = {
        "Apple": {"price": 0.99, "stock": 50, "initial_stock": 50, "image": "https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?w=300&h=300&fit=crop"},
        "Banana": {"price": 0.49, "stock": 40, "initial_stock": 40, "image": "https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?w=300&h=300&fit=crop"},
        "Milk (1L)": {"price": 1.89, "stock": 25, "initial_stock": 25, "image": "https://images.unsplash.com/photo-1563636619-e9143da7973b?w=300&h=300&fit=crop"},
        "Bread": {"price": 2.49, "stock": 15, "initial_stock": 15, "image": "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=300&h=300&fit=crop"},
        "Eggs (12pk)": {"price": 3.99, "stock": 30, "initial_stock": 30, "image": "https://images.unsplash.com/photo-1516448620398-c5f44bf9f441?w=300&h=300&fit=crop"},
        "Cheese": {"price": 4.50, "stock": 20, "initial_stock": 20, "image": "https://images.unsplash.com/photo-1486297678162-eb2a19b0a32d?w=300&h=300&fit=crop"},
        "Strawberries": {"price": 2.99, "stock": 35, "initial_stock": 35, "image": "https://images.unsplash.com/photo-1464965911861-746a04b4bca6?w=300&h=300&fit=crop"},
        "Blueberries": {"price": 3.49, "stock": 25, "initial_stock": 25, "image": "https://images.unsplash.com/photo-1601004890684-d8cbf643f5f2?w=300&h=300&fit=crop"},
        "Orange Juice": {"price": 2.99, "stock": 18, "initial_stock": 18, "image": "https://images.unsplash.com/photo-1621506289937-a8e4df240d0b?w=300&h=300&fit=crop"},
        "Coffee Beans": {"price": 8.99, "stock": 12, "initial_stock": 12, "image": "https://images.unsplash.com/photo-1447933601403-0c6688de566e?w=300&h=300&fit=crop"},
        "Tea Bags (80pk)": {"price": 3.20, "stock": 40, "initial_stock": 40, "image": "https://images.unsplash.com/photo-1576092768241-dec231879fc3?w=300&h=300&fit=crop"},
        "Chocolate Bar": {"price": 1.50, "stock": 60, "initial_stock": 60, "image": "https://images.unsplash.com/photo-1511381939415-e44015466834?w=300&h=300&fit=crop"},
        "Potato Chips": {"price": 1.99, "stock": 45, "initial_stock": 45, "image": "https://images.unsplash.com/photo-1566478989037-eec170784d0b?w=300&h=300&fit=crop"},
        "Pasta (500g)": {"price": 1.20, "stock": 50, "initial_stock": 50, "image": "https://images.unsplash.com/photo-1551462147-ff29053bfc14?w=300&h=300&fit=crop"},
        "Rice (1kg)": {"price": 2.10, "stock": 40, "initial_stock": 40, "image": "https://images.unsplash.com/photo-1586201375761-83865001e31c?w=300&h=300&fit=crop"},
        "Olive Oil": {"price": 6.49, "stock": 15, "initial_stock": 15, "image": "https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?w=300&h=300&fit=crop"},
        "Butter": {"price": 2.50, "stock": 22, "initial_stock": 22, "image": "https://images.unsplash.com/photo-1589985270826-4b7bb135bc9d?w=300&h=300&fit=crop"},
        "Yogurt": {"price": 0.85, "stock": 48, "initial_stock": 48, "image": "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=300&h=300&fit=crop"},
        "Ice Cream": {"price": 4.99, "stock": 14, "initial_stock": 14, "image": "https://images.unsplash.com/photo-1497034825429-c343d7c6a68f?w=300&h=300&fit=crop"}
    }

if "basket" not in st.session_state:
    st.session_state.basket = {}

tab1, tab2 = st.tabs(["Storefront", "Stock management"])

with tab1:
    st.header("Shop our products!")
    
    items = list(st.session_state.inventory.keys())
    chunked_items = [items[i:i + 3] for i in range(0, len(items), 3)]
    
    for row in chunked_items:
        cols = st.columns(3)
        for i, item_name in enumerate(row):
            with cols[i]:
                item_data = st.session_state.inventory[item_name]
                
                st.image(item_data["image"], use_container_width=True)
                st.subheader(item_name)
                st.write(f"**Price:** £{item_data['price']:.2f}")
                st.write(f"Available Stock: {item_data['stock']}")
                
                if item_data["stock"] > 0:
                    if st.button(f"Add {item_name} to basket", key=f"add_{item_name}"):
                        st.session_state.inventory[item_name]["stock"] -= 1
                        st.session_state.basket[item_name] = st.session_state.basket.get(item_name, 0) + 1
                        st.rerun()
                else:
                    st.error("Out of stock")
                    
    st.markdown("---")
    
    st.header("Your shopping basket")
    if not st.session_state.basket:
        st.write("Your basket is empty.")
    else:
        total_cost = 0.0
        for item_name, quantity in st.session_state.basket.items():
            price = st.session_state.inventory[item_name]["price"]
            item_total = price * quantity
            total_cost += item_total
            st.write(f"• **{item_name}** x{quantity} — £{item_total:.2f}")
            
        st.write(f"Total: £{total_cost:.2f}")
        
        if st.button("Proceed to Checkout", type="primary"):
            st.session_state.checkout_success = f"Order successful!! Your total is £{total_cost:.2f}. (I'm not taking money from you for a fake supermarket website teehee.)"
            st.session_state.basket = {}
            st.rerun()

    if "checkout_success" in st.session_state:
        st.success(st.session_state.checkout_success)
        if st.session_state.basket:
            del st.session_state.checkout_success

with tab2:
    st.header("Inventory & Restock Controls")
    
    col_h1, col_h2, col_h3 = st.columns([2, 1, 1])
    with col_h1:
        st.markdown("Product")
    with col_h2:
        st.markdown("Current Stock")
    with col_h3:
        st.markdown("Actions")
    st.markdown("---")
    
    for item_name, item_data in st.session_state.inventory.items():
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            st.write(item_name)
        with col2:
            st.write(str(item_data["stock"]))
        with col3:
            init_val = item_data["initial_stock"]
            if st.button(f"Reset to {init_val}", key=f"restock_{item_name}", use_container_width=True):
                st.session_state.inventory[item_name]["stock"] = init_val
                st.success(f"{item_name} restocked to {init_val}!")
                st.rerun()