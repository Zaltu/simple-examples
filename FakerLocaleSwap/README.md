# Fakerer
Faker is designed in such a way that you absolutely need to generate a brand new `Faker` object is you want to change locales.  
IMO this is stupid. For any user-facing application, you don't want to regenerate a new instance each time, there's no logistical reason to. This simple example adds a function to swap the locale of a Faker instance after it has been created.

Unfortunately, once again due to the way Faker is designed, this model is entirely thread-unsafe. It's still a good example, which is why it's here, but there's no good way of integrating this into a real application.