-- my-mod
-- https://github.com/WhoIsSethDaniel/mason-tool-installer.nvim
return {
  {
    "WhoIsSethDaniel/mason-tool-installer.nvim",
    opts = {
      ensure_installed = {
        "lua-language-server", -- Lua LSP
        "stylua", -- Lua formatter
        "python-lsp-server", -- Python LSP
        "prettier", -- Formatter for JavaScript/TypeScript
        "eslint_d", -- Linter for JavaScript/TypeScript
        "codelldb", -- Debugger for Rust/C/C++
        "jedi-language-server"
        "rust-analyzer"
        -- Add other tools as needed
      },
      auto_update = true, -- Automatically update tools
      run_on_start = true, -- Install tools on Neovim startup
      start_delay = 3000, -- Delay in milliseconds before installation starts
    },
  },
}
