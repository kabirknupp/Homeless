from RightmoveScraper import RightmoveScraper

class Main:

    """
    """

    def __init__(self):
        self.scraper = RightmoveScraper()

    def main(self):
        """
        main method downloads and saves the data.
        """
        self.scraper.run()
        
    
if __name__ == "__main__":
    main = Main()
    main.main()