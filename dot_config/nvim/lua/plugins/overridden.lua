-- ailac22-mine
-- ChatGPT + https://docs.astronvim.com/configuration/customizing_plugins/
return {
  "AstroNvim/astrocore",
  ---@type AstroCoreOpts
  opts = {
    rooter = {
      autochdir = true, -- enable automatic directory change
    },
    options = {
      opt = {
        wrap = true, -- enable line wrapping
      },
    },
  },
}

