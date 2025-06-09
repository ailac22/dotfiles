return {
  "nvim-neo-tree/neo-tree.nvim",
  opts = function(_, opts)
    opts.window = opts.window or {}
    opts.window.width = 50 -- set this to your desired width (default is 40)
  end,
}
