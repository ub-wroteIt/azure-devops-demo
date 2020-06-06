resource "azurerm_network_interface" "main" {
  name                = "${var.application_type}-${var.resource_type}-nic"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group_name}"

  ip_configuration {
    name                          = "internal"
    subnet_id                     = "${output.subnet_id_test}"
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = "${output.public_ip_address_id}"
  }
}

resource "azurerm_linux_virtual_machine" "" {
  name                = "${var.application_type}-${var.resource_type}-vm"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group_name}"
  size                = "Standard_B1s"
  admin_username      = "superheroadmin"
  network_interface_ids = [azurerm_network_interface.main.id]
  admin_ssh_key {
    username   = "adminuser"
    public_key = file("~/.ssh/id_rsa.pub")
  }
  os_disk {
    caching           = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "16.04-LTS"
    version   = "latest"
  }
}
