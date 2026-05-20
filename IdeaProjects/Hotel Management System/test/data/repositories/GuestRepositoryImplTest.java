package data.repositories;

import data.models.Guest;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;


public class GuestRepositoryImplTest {

    @Test
    public void testThatRepositoryCanBeCreated()   {

        GuestRepository repository = new GuestRepositoryImpl();
        assertNotNull(repository);
    }

    @Test
    public void testThatRepositoryCountIsZero() {

        GuestRepository repository = new GuestRepositoryImpl();
        assertEquals (0, repository.count());
    }

    @Test
    public void testThatRepositoryCanSaveGuest()    {

        GuestRepository repository = new GuestRepositoryImpl();
        Guest guest = new Guest("Toby", "08183215687", "oluwatoby007@gmail.com");
        repository.save(guest);
        assertEquals(1, repository.count());
    }

    @Test
    public void testThatSavedGuestCanBeFoundById()    {

        GuestRepository repository = new GuestRepositoryImpl();

        Guest guest = new Guest("Kylian", "08183215687", "kylianmbappe@gmail.com");
        repository.save(guest);
        Guest findGuest = repository.findById(guest.getId());
        assertEquals("Kylian", findGuest.getName());

    }

    @Test
    public void testThatGuestCanBeDeletedById()     {
        GuestRepository repository = new GuestRepositoryImpl();
        Guest guest = new Guest("Deborah", "08183215687", "debby007@gmail.com");
        repository.save(guest);
        assertEquals(1, repository.count());
        repository.deleteById(guest.getId());
        assertEquals(0, repository.count());
    }

    @Test
    public void testThatRepositoryCanHoldMoreThanOneGuest() {

        GuestRepository repository =
                new GuestRepositoryImpl();

        Guest firstGuest =
                new Guest("Toby", "08183215687", "toby@gmail.com"
                );

        Guest secondGuest =
                new Guest("Kylian", "09000000000", "kylian@gmail.com"
                );

        repository.save(firstGuest);
        repository.save(secondGuest);

        assertEquals(2, repository.count());

    }


    @Test
    public void testThatRepositoryCountDecreasesAfterDeletingGuest() {

        GuestRepository repository =
                new GuestRepositoryImpl();

        Guest firstGuest =
                new Guest("Toby", "08183215687", "toby@gmail.com"
                );

        Guest secondGuest =
                new Guest("Kylian", "09000000000", "kylian@gmail.com"
                );

        repository.save(firstGuest);
        repository.save(secondGuest);

        assertEquals(2, repository.count());

        repository.deleteById(firstGuest.getId());

        assertEquals(1, repository.count());
    }

    @Test
    public void testThatDeletedGuestCannotBeFound() {

        GuestRepository repository =
                new GuestRepositoryImpl();

        Guest guest =
                new Guest("Toby", "08183215687", "toby@gmail.com"
                );

        repository.save(guest);

        repository.deleteById(guest.getId());

        Guest findGuest =
                repository.findById(guest.getId());

        assertNull(findGuest);
    }

    @Test
    public void testThatSavingSameGuestTwiceDoesNotIncreaseCount() {

        GuestRepository repository =
                new GuestRepositoryImpl();

        Guest guest =
                new Guest(
                        "Toby", "08183215687", "toby@gmail.com"
                );

        repository.save(guest);
        repository.save(guest);

        assertEquals(1, repository.count());
    }

    @Test
    public void testThatGuestDetailsCanBeUpdated() {

        GuestRepository repository =
                new GuestRepositoryImpl();

        Guest guest =
                new Guest(
                        "Toby", "08183215687", "toby@gmail.com");

        repository.save(guest);

        guest.setPhoneNumber("07043537005");

        repository.save(guest);

        Guest updatedGuest =
                repository.findById(guest.getId());

        assertEquals(
                "07043537005", updatedGuest.getPhoneNumber());
    }

    @Test
    public void testThatCorrectGuestIsFoundWhenTwoGuestsAreSaved() {
        GuestRepository repository = new GuestRepositoryImpl();

        Guest firstGuest = new Guest("Toby", "08183215687", "toby@gmail.com");
        Guest secondGuest = new Guest("Kylian", "09000000000", "kylian@gmail.com");

        repository.save(firstGuest);
        repository.save(secondGuest);

        Guest foundGuest = repository.findById(secondGuest.getId());

        assertEquals("Kylian", foundGuest.getName());
    }
}
